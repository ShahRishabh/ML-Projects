Z = zeros(77760,11,15);
Z_rep = zeros(77760,15);

for i = 1:15
    for j = 1:11
        a = 'ubject';
        c = '.png';
        if j == 1
            b = 'cl';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 2
            b = 'glass';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 3
            b = 'happy';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 4
            b = 'll';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 5
            b = 'ng';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 6
            b = 'norm';
            if i <= 9
                a = strcat('0',num2str(i));                
            else
                a = num2str(i);
            end
        elseif j == 7
            c = '.rightlight';
            if i <= 9
                b = strcat('0',num2str(i));                
            else
                b = num2str(i);
            end
        elseif j == 8
            c = '.sad';
            if i <= 9
                b = strcat('0',num2str(i));                
            else
                b = num2str(i);
            end
        elseif j == 9
            c = '.sleepy';
            if i <= 9
                b = strcat('0',num2str(i));                
            else
                b = num2str(i);
            end
        elseif j == 10
            c = '.surprised';
            if i <= 9
                b = strcat('0',num2str(i));                
            else
                b = num2str(i);
            end
        elseif j == 11
            c = '.wink';
            if i <= 9
                b = strcat('0',num2str(i));                
            else
                b = num2str(i);
            end
        end
        path = strcat('E:\Studies\CH5440\Assignments\Assign 2\assignment2_data\yalefaces\yalefaces\s',a,b,c);
        img = imread(path);
        Z(:,j,i) = reshape(img,[77760 1]);
    end
    Z(:,:,i) = Z(:,:,i) - mean(Z(:,:,i));
end

Z = Z./255; % Normalizing the data

for i = 1:15
    [u,s,v] = svd(Z(:,:,i),'econ');
    v_rep = v(1,:); % Taking eigenvec corr to highest singular value
    Z_rep(:,i) = u(:,1)*s(1,:)*v(1,:)';
end

correct = 0;

for i = 1:15
    for j = 1:11
        error = Inf;
        index = -1;
        for k = 1:15
            l2_norm = norm(Z(:,j,i)-Z_rep(:,k),2);
            if l2_norm < error
                error = l2_norm;
                index = k;
            end
        end
        if index == i
            correct = correct+1;
        end
    end
end